import axios from 'axios';
import { API_URL } from '../constants';
import { ICalendarRequest } from '../../interfaces/sendCalendar.interface';


const instance = axios.create({
  baseURL: API_URL,
});

export function sendCalendar(data:ICalendarRequest) {
  return instance.post('/calendar', data);
}
