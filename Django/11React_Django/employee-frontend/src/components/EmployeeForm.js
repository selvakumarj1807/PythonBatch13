import React, { useState, useEffect } from "react";
import { createEmployee, updateEmployee } from "../services/api";

function EmployeeForm({ selected, refresh }) {
  const [form, setForm] = useState({
    fullName: "",
    salary: "",
    departmentID: "",
  });

  useEffect(() => {
    if (selected) setForm(selected);
  }, [selected]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (form.employeeId) {
      await updateEmployee(form.employeeId, form);
    } else {
      await createEmployee(form);
    }

    setForm({ fullName: "", salary: "", departmentID: "" });
    refresh();
  };

  return (
    <div>
      <h2>{form.employeeId ? "Update" : "Add"} Employee</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="fullName"
          placeholder="Name"
          value={form.fullName}
          onChange={handleChange}
          required
        />
        <br />

        <input
          type="number"
          name="salary"
          placeholder="Salary"
          value={form.salary}
          onChange={handleChange}
          required
        />
        <br />

        <input
          type="number"
          name="departmentID"
          placeholder="Department"
          value={form.departmentID}
          onChange={handleChange}
          required
        />
        <br />

        <button type="submit">Save</button>
      </form>
    </div>
  );
}

export default EmployeeForm;