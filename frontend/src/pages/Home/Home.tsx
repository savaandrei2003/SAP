import React, { useEffect, useState } from 'react';
import Page from '../../common/components/Page/Page'
import '../../index.css'
import './home.css'


import Card from './components/Card';
import { ICard } from '../../common/interfaces/card.interface';
import { IHome } from '../../common/interfaces/home.interface';
import Salut from './components/Salut';
import Status from './components/Status';
import { getHome, postBoth } from '../../common/services/api/home';
import ProductID from './InputFields';
import CalendarComponent from './Calendar';
import { postProduct } from '../../common/services/api/postProduct';


export default function Home() {

  const [prodId, setProdID] = useState<string>("");
  const [calendar, setCalendar] = useState<Date | null>(null);
  const [info1, setInfo1] = useState<string>("");
  const [info2, setInfo2] = useState<string>("");

  const [isLoading, setIsLoading] = useState(false);

  const handleClick = async () => {
    try {
    const values = { time : calendar, prod_id: prodId };
    console.log(values);
    const response = await postBoth(values);

  setInfo1(response.data["info1"]);
  setIsLoading(true);
  setProdID("");

//   console.log(response.data["duration"]);
} catch (e) {
  console.error(e);
}
};





    return (
    <Page>
      <div className='flex flex-col items-center justify-center h-screen mx-36'>
        <div className='flex flex-row h-4/5 div-gri w-full'>
          <div className='flex flex-col  py-5 h-full w-full items-center justify-strat'>
            
            <div className='flex flex-col text-white  w-full items-end mb-3'>
              <div className='flex fontus main-title'>DASH</div>
            </div>
            <div className='flex flex-row  h-1/3 w-5/6 items-center justify-around mb-5  '>
              <div className='flex flex-col text-white w-2/3 h-full new mr-3 rounded items-center justify-center  '><ProductID /></div>
              <div className='flex flex-col text-white w-1/3 h-full new ml-3 rounded items-center justify-around'><CalendarComponent /></div>   
            </div>
            <div className='flex flex-ocl h-1/3 w-5/6 items-center justify-center '>
              <div className='flex flex-col text-white w-full h-full numaipot  rounded'></div>   
            </div>
          </div>


          <div className='flex flex-col py-5 h-full w-full bg-white items-center '>
            <div className='flex flex-col  w-full items-start justify-center '>
              <div className='flex flex-col text-white  w-full items-start mb-5'> 
                <div className='flex fontus calitate2'>BOARD</div>
              </div>
       
            </div>
            <div className='flex flex-col  h-1/3 w-full items-center justify-around mb-5 '>
              <div className='flex flex-col text-white h-1/3 w-3/4 h-full new mr-3 items-center justify-around rounded'></div>
            </div>
            <div className='flex flex-row  h-1/3 w-5/6 items-center justify-center mb-2 '>
              <div className='flex flex-col text-white w-1/3 h-full new m-3 rounded'></div>
              <div className='flex flex-col text-white w-1/3 h-full new m-3 rounded'></div>  
            </div>

          </div>
        </div>
      </div>
        
      
      
       
     {/*  <div className='sm:mb-10'>
            <div className='flex flex-col items-center justify-center'>
                <Salut 
                user_name={homeInfo.user_name}
                location_home={homeInfo.location_home}
                />

            </div>
            
            <div className="w-full  flex flex-col items-center justify-center" >
                <Status 
                index_home={homeInfo.index_home} 
                    />
            </div>

       </div>
            
            
        <div className='flex flex-col w-5/6 sm:w-1/2 mb-20 sm:mb-28 lg:w-1/3 '>

            {!isLoading ? (
            !isError && homeInfo.cards.length !== 0 ? (
              <div >
                {homeInfo.cards.map((home: ICard) => (
                  <Card
                    key={home.index}
                    name={home.name}
                    location={home.location}
                    hour={home.hour}
                    temperature={home.temperature}
                    index={home.index}
                    
                  />
                ))}
              </div>
                ) : (
                  <p>Esti prost</p>
                )
              ) : (
                <p>Bravo</p>
            )}

            

        </div>
        
        
    </div>  */}
        
   </Page>
    );

}
