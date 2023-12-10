import React from 'react';
import './page.css';

interface IPageProps {
  children: JSX.Element;
}

export default function Page({ children }: IPageProps) {

  return (
    <div className='page flex flex-col '>
      <div className="">{children}</div>
    </div>
  );
}
