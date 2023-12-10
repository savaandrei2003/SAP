import axios from 'axios';
import { API_URL } from '../constants';

const instance = axios.create({
  baseURL: API_URL,
});


export function postTarget() {
  return instance.post('/targeted-message');
}