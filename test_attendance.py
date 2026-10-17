import unittest


class AttendanceSystem:
    def __init__(self):
        self.records = {}

    def mark_attendance(self, student_id, date):
        key = (student_id, date)

        if not student_id:
            return "Invalid student ID"

        if key in self.records:
            return "Attendance already marked"

        self.records[key] = "Present"
        return "Attendance marked successfully"


class TestAttendance(unittest.TestCase):

    def setUp(self):
        self.system = AttendanceSystem()

    def test_mark_attendance(self):
        result = self.system.mark_attendance(
            "STU001", "2026-10-17"
        )
        self.assertEqual(
            result, "Attendance marked successfully"
        )

    def test_duplicate_attendance(self):
        self.system.mark_attendance("STU001", "2026-10-17")
        result = self.system.mark_attendance(
            "STU001", "2026-10-17"
        )
        self.assertEqual(
            result, "Attendance already marked"
        )

    def test_empty_student_id(self):
        result = self.system.mark_attendance("", "2026-10-17")
        self.assertEqual(result, "Invalid student ID")


if __name__ == "__main__":
    unittest.main()
