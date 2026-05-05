import React, { useEffect, useState } from "react";
import { getEmployees, deleteEmployee } from "../services/api";

function EmployeeList({ onEdit }) {
  const [employees, setEmployees] = useState([]);

  const fetchData = async () => {
    const res = await getEmployees();
    setEmployees(res.data);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDelete = async (id) => {
    await deleteEmployee(id);
    fetchData();
  };

  return (
    <div>
      <h2>Employee List</h2>
      <table border="1" width="100%">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Salary</th>
            <th>Dept</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((emp) => (
            <tr key={emp.employeeId}>
              <td>{emp.employeeId}</td>
              <td>{emp.fullName}</td>
              <td>{emp.salary}</td>
              <td>{emp.departmentID}</td>
              <td>
                <button onClick={() => onEdit(emp)}>Edit</button>
                <button onClick={() => handleDelete(emp.employeeId)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EmployeeList;