import React, { useState, useEffect } from 'react';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { sendCalendar } from '../../common/services/api/calendar';

interface CalendarComponentProps {
  initialDate?: Date; // Adaugăm prop-ul pentru data inițială
}

const CalendarComponent: React.FC<CalendarComponentProps> = ({ initialDate }) => {
    
    const [selectedDate, setSelectedDate] = useState<Date | null>(
      initialDate || new Date()
    );
    const [isCalendarOpen, setIsCalendarOpen] = useState(false);

    const [hasBeenSearched, setHasBeenSearched] = useState<boolean>(false);
    const [info, setInfo] = useState<string>("");
    

    const handleClick = async () => {
        try {
        const values = { time: selectedDate };
        console.log(values);
        const response = await sendCalendar(values);

      setInfo(response.data["info"]);
      setHasBeenSearched(true);
      setSelectedDate(null);

    //   console.log(response.data["duration"]);
      
    } catch (e) {
      console.error(e);
    }
  };

    
  
  
    const handleDateChange = (date: Date | null) => {
      setSelectedDate(date);
    };
  
    const openCalendar = () => {
      setIsCalendarOpen(true);
    };
  
    const closeCalendar = () => {
      setIsCalendarOpen(false);
    };
  
    return (
      <div className='flex flex-col text-white h-1/3 w-3/4 h-full mx-3 rounded items-center justify-around p-4'>
        <div className='flex flex-row tems-center justify-center'>
            <div className="flex flex-col items-center justify-center mt-2">
                <button className="bg-red-500 flex box-shape items-center justify-center p-2 mb-2" onClick={openCalendar}>
                    <img 
                    src={"https://img.icons8.com/ios-filled/50/ffffff/calendar--v1.png"}
                    alt="Calendar Icon"
                    className="text-white w-10 h-10"
                    />
                </button>
           
                <DatePicker
                selected={selectedDate}
                onChange={handleClick}
                dateFormat="dd/MM/yyyy"
                className="rounded bg-white text-black p-2 flex flex-col items-center justify-center w-full"
                open={isCalendarOpen}
                onClickOutside={closeCalendar}
                />
            </div>
        </div>
        
        
    </div>
    );
  };
  
  export default CalendarComponent;