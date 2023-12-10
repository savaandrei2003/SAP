import axios from 'axios';
import { API_URL } from '../constants';
import { IGenericRequest } from '../../interfaces/generic.interface';

const instance = axios.create({
  baseURL: API_URL,
});


export function postGeneric(data:IGenericRequest) {
  return instance.post('/general-message-to-costumer', data);
}
