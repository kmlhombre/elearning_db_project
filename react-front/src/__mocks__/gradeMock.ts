import { Grade } from "../models/Grade";

export const gradeMock: Grade = {
  id: 1,
  note: 4,
  subject: "Historia",
};

export const gradeMockArray: Grade[] = Array(10)
  .fill(gradeMock)
  .map((grade: Grade, index) => ({
    ...grade,
    id: grade.id + index,
  }));
