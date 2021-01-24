import { UserModel } from "../../models/UserModel";
import createAsyncSlice from "../createAsyncSlice";

export const UserSlice = createAsyncSlice<
  UserModel,
  { email: string; password: string }
>({
  name: "userSlice",
});
