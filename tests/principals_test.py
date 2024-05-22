from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get("/principal/assignments", headers=h_principal)

    assert response.status_code == 200

    data = response.json["data"]
    for assignment in data:
        assert assignment["state"] in [
            AssignmentStateEnum.SUBMITTED,
            AssignmentStateEnum.GRADED,
        ]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        "/principal/assignments/grade",
        json={"id": 5, "grade": GradeEnum.A.value},
        headers=h_principal,
    )

    assert response.status_code == 400, f"{response.json}"

    data = response.json

    assert data["error"] == "FyleError"


def test_grade_assignment(client, h_principal):
    response = client.post(
        "/principal/assignments/grade",
        json={"id": 4, "grade": GradeEnum.C.value},
        headers=h_principal,
    )

    assert response.status_code == 200

    assert response.json["data"]["state"] == AssignmentStateEnum.GRADED.value
    assert response.json["data"]["grade"] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        "/principal/assignments/grade",
        json={"id": 4, "grade": GradeEnum.B.value},
        headers=h_principal,
    )

    assert response.status_code == 200

    assert response.json["data"]["state"] == AssignmentStateEnum.GRADED.value
    assert response.json["data"]["grade"] == GradeEnum.B


def test_get_all_teachers(client, h_principal):
    response = client.get("/principal/teachers", headers=h_principal)

    assert response.status_code == 200

    data = response.json["data"]
    for teacher in data:
        assert len(teacher.keys()) == 4

    assert len(data) == 2


def test_grade_assignment_invalid_grade(client, h_principal):
    """
    failure case: API should allow only grades available in enum
    """
    response = client.post(
        "/principal/assignments/grade",
        json={
            "id": 3,
            "grade": "N",  # Invalid grade
        },
        headers=h_principal,
    )

    assert response.status_code == 400


def test_grade_invalid_assignment(client, h_principal):
    """
    failure case: API should allow only valid assignment ids
    """
    response = client.post(
        "/principal/assignments/grade",
        json={"id": -17, "grade": GradeEnum.C.value},
        headers=h_principal,
    )

    assert response.status_code == 404

    data = response.json

    assert data["error"] == "FyleError"


def test_grade_missing_grade(client, h_principal):
    """
    failure case: grade cannot be null
    """
    response = client.post(
        "/principal/assignments/grade", json={"id": 3}, headers=h_principal
    )

    assert response.status_code == 400

    data = response.json

    assert data["error"] == "ValidationError"


def test_grade_missing_id(client, h_principal):
    """
    failure case: id cannot be null
    """
    response = client.post(
        "/principal/assignments/grade",
        json={"grade": GradeEnum.A.value},
        headers=h_principal,
    )

    assert response.status_code == 400

    data = response.json

    assert data["error"] == "ValidationError"


def test_unauthorized_principal(client):
    """
    failure case: unauthorized principal should not be allowed to access any endpoint
    """