export class UserModel {
  public readonly type!: "student  | teacher | parent";
  public readonly name!: string;
  public readonly lastname!: string;
  public readonly year?: number;
}

export interface LoginRequest {
  email: string;
  password: string;
}
