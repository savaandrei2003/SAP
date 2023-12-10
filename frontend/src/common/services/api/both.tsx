import axios from 'axios';
import { API_URL } from '../constants';
import { IBothRequest } from '../../interfaces/both.interface';

const instance = axios.create({
  baseURL: API_URL,
});


export function postBoth(data:IBothRequest) {
  return instance.post('/product-prediction', data);
}
