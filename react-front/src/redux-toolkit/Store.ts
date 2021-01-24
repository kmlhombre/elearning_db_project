import {
  combineReducers,
  configureStore,
  getDefaultMiddleware,
} from "@reduxjs/toolkit";
import { createEpicMiddleware, Epic } from "redux-observable";
import { Persistor, persistReducer, persistStore } from "redux-persist";
import storage from "redux-persist/lib/storage";
import { ActionType } from "typesafe-actions";
import { rootEpic } from "../redux-toolkit/epics/RootEpic";
import { UserSlice } from "../redux-toolkit/slice/UserSlice";
import { IServices, Services as Dependencies } from "../services";

export const rootReducer = combineReducers({
  userSlice: UserSlice.reducer,
});

export type RootState = ReturnType<typeof rootReducer>;
export type RootAction = ActionType<typeof UserSlice.actions>;

export type RootEpicType = Epic<RootAction, RootAction, RootState, IServices>;

const persistConfig = {
  key: "root",
  storage,
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

const epicMiddleware = createEpicMiddleware<
  RootAction,
  RootAction,
  RootState,
  IServices
>({
  dependencies: Dependencies,
});

const store = configureStore({
  reducer: persistedReducer,
  middleware: [
    ...getDefaultMiddleware({
      serializableCheck: false,
    }),
    epicMiddleware,
  ],
});

const persistor: Persistor = persistStore(store);

export { store, persistor };

epicMiddleware.run(rootEpic);
