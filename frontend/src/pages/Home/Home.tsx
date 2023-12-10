import React, { useEffect, useState } from 'react';
import Page from '../../common/components/Page/Page'
import '../../index.css'
import './home.css'


import Card from './components/Card';
import { ICard } from '../../common/interfaces/card.interface';
import { IHome } from '../../common/interfaces/home.interface';
import Salut from './components/Salut';
import Status from './components/Status';
import { getHome } from '../../common/services/api/home';
import ProductID from './InputFields';
import CalendarComponent from './Calendar';
import { postProduct } from '../../common/services/api/postProduct';
import { IBothRequest } from '../../common/interfaces/both.interface';
import { postBoth } from '../../common/services/api/both';
import { postGeneric } from '../../common/services/api/postGeneralMail';
import { postTarget } from '../../common/services/api/target';
import { postGenericEmployee } from '../../common/services/api/genericEmployee';


export default function Home() {
  const [data, setData] = useState<Date | null>(new Date());
  const [id, setId] = useState<string>("");

 const [info1,setInfo1] = useState<string>("");
 const [info2,setInfo2] = useState<string>("");

 const [product, setProduct] = useState<string>("");
 const [percentage, setPercentage] = useState<string>("");

  const [productEmployee, setProductEmployee] = useState<string>("");
  const [percentageEmployee, setPercentageEmployee] = useState<string>("");

  const handleClick = async () => {
    const values = { date:data, product_id: id};
    console.log(values);
    const response = await postBoth(values);
  };

  const onProductChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setProduct(event.target.value);
  }

  const onPercentageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setPercentage(event.target.value);
  }

  const handleSubmitMail = async () => {
    const values = { product: product, percentage:percentage};
    console.log(values);
    const response = await postGeneric(values);
    console.log(response);
  }

  const handleSubmitTarget = async () => {
    const response = await postTarget();
    console.log(response);
  }

  const handleSubmitMailEmployee = async () => {
    const values = { product: productEmployee, percentage:percentageEmployee};
    console.log(values);
    const response = await postGenericEmployee(values);
    console.log(response);
  }
  
  return (
    <Page>
      <div className='flex flex-col items-center justify-center h-screen mx-36'>
        <div className='flex flex-row h-4/5 div-gri w-full'>
          <div className='flex flex-col  py-5 h-full w-full items-center justify-strat'>
            
            <div className='flex flex-col text-white  w-full items-end mb-3'>
              <div className='flex fontus main-title'>DASH</div>
            </div>
            <div className='flex flex-row  h-1/3 w-5/6 items-center justify-around mb-5  '>
              <div className='flex flex-col text-white w-2/3 h-full new mr-3 rounded items-center justify-center  '><ProductID callback={setId}/></div>
              <div className='flex flex-col text-white w-1/3 h-full new ml-3 rounded items-center justify-around'><CalendarComponent callback={setData} /></div>   
            </div>
            <div className='flex flex-ocl h-1/3 w-5/6 items-center justify-center '>
              <div className='flex flex-col w-full h-full numaipot  rounded'>
                <input value={product} onChange={onProductChange}/>
                <input value={percentage} onChange={onPercentageChange}/>
                <button onClick={handleSubmitMail}>Trimite</button>

              </div>   
            </div>
          </div>


          <div className='flex flex-col py-5 h-full w-full bg-white items-center '>
            <div className='flex flex-col  w-full items-start justify-center '>
              <div className='flex flex-col text-white  w-full items-start mb-5'> 
                <div className='flex fontus calitate2'>BOARD</div>
              </div>
       
            </div>
            <div className='flex flex-col  h-1/3 w-full items-center justify-around mb-5 '>
              <div className='flex flex-col h-1/3 w-3/4 h-full new mr-3 items-center justify-around rounded'>
                <button className='bg_color text-white p-2 rounded-lg w-1/2' onClick={handleSubmitTarget}>Trimite mesaje targetate</button>
              </div>
            </div>
            <div className='flex flex-row  h-1/3 w-5/6 items-center justify-center mb-2 '>
              <div className='flex flex-col w-1/3 h-full new m-3 rounded justify-center items-center'>
                <input value={productEmployee} onChange={(event) => setProductEmployee(event.target.value)}/>
                <input value={percentageEmployee} onChange={(event) => setPercentageEmployee(event.target.value)}/>
                <button className='bg_color text-white p-2 rounded-lg w-1/2 justify-center items-center' onClick={handleSubmitMailEmployee}>Trimite la angajati</button>
              </div>

            </div>
            <div className='flex flex-col items-center justify-center' ><button onClick={handleClick} className='bg_color text-white p-2 rounded-lg w-full'>trimite</button></div>

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
