import ApiService from "../services/ApiService";

export interface IServices {
  api: typeof ApiService;
}

export const Services: IServices = {
  api: ApiService,
};
