/* eslint-disable import/no-anonymous-default-export */
import {
  createSlice,
  PayloadAction,
  SliceCaseReducers,
  ValidateSliceCaseReducers,
} from "@reduxjs/toolkit";

export interface IState<T> {
  data: T | null;
  loading: boolean;
  error: boolean;
  message: string | null;
}

export const CANCEL_MESSAGE = "cancelled";

export default <
  TData,
  TPayload = undefined,
  Reducers extends SliceCaseReducers<IState<TData>> = SliceCaseReducers<
    IState<TData>
  >
>({
  name,
  initialState = { data: null, loading: false, error: false, message: null },
  inboundDataTransformer,
  reducers,
}: {
  name: string;
  initialState?: IState<TData>;
  inboundDataTransformer?: (data: TData | null) => TData | null;
  reducers?: ValidateSliceCaseReducers<IState<TData>, Reducers>;
}) => {
  return {
    ...createSlice({
      name,
      initialState,
      reducers: {
        start: (state, _action: PayloadAction<TPayload>) => {
          state.loading = true;
          state.error = false;
        },
        fulfilled: (state, action: PayloadAction<TData>) => ({
          ...state,
          loading: false,
          data: action.payload,
          error: false,
          message: null,
        }),
        set: (state, action: PayloadAction<TData>) => ({
          ...state,
          loading: false,
          data: action.payload,
          error: false,
          message: null,
        }),
        reset: (state) => ({
          ...state,
          loading: false,
          data: null,
          error: false,
          message: null,
        }),
        rejected: (state, action: PayloadAction<string>) => {
          state.loading = false;
          state.error = true;
          state.message = action.payload;
        },
        cancel: (state) => {
          state.loading = false;
          state.error = true;
          state.message = CANCEL_MESSAGE;
        },
        ...reducers,
      },
    }),
  };
};
