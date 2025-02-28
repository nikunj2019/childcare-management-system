import { useEffect, useState } from "react";
import { getEnrollments } from "../services/api";

const EnrollmentList = () => {
  const [enrollments, setEnrollments] = useState([]);

  useEffect(() => {
    getEnrollments().then((res) => setEnrollments(res.data));
  }, []);

  return (
    <div>
      <h2 className="text-xl font-bold mb-2">📝 Enrolled Children</h2>
      <ul className="bg-white p-4 rounded shadow-md">
        {enrollments.map((child) => (
          <li key={child.id} className="border-b py-2">
            {child.name} - {child.classroom}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EnrollmentList;