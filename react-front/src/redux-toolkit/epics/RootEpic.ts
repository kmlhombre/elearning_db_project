import { combineEpics } from "redux-observable";
import { RootAction, RootState } from "../../redux-toolkit/Store";
import { IServices } from "../../services";

export const rootEpic = combineEpics<
  RootAction,
  RootAction,
  RootState,
  IServices
>();
// add here epics
