import { Grade } from "../../../models/Grade";
import "./../../../stylesheet/Grade.scss";

interface IProps {
  title?: string;
  subtitle?: string;
  grade?: Grade;
}

function GradeRow({ title, subtitle, grade }: IProps) {
  return (
    <div className="d-flex flex-row grade-container justify-content-around">
      {title ? <p>{title}</p> : null}
      {subtitle ? <p>{subtitle}</p> : null}
      {grade?.subject ? <p>{grade.subject}</p> : null}
      {grade?.note ? <p>{grade.note}</p> : null}
    </div>
  );
}

export default GradeRow;
