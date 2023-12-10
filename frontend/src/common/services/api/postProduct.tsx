import axios from 'axios';
import { API_URL } from '../constants';
import { IProductRequest } from '../../interfaces/coordinates.interface';

const instance = axios.create({
  baseURL: API_URL,
});

export function postProduct(data:IProductRequest) {
  return instance.post('/products', data);
}
