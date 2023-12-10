    import React, { useState } from "react";


    // import "./animatie.css";
    import "./home.css";
    import { postProduct } from "../../common/services/api/postProduct";

    function ProductID() {
    const [x, setX] = useState<string>("");
    const [hasBeenSearched, setHasBeenSearched] = useState<boolean>(false);
    const [mapsLink, setMapsImage] = useState<string>("");
    

    const handleClick = async () => {
        try {
        const values = { product_id: x };
        console.log(values);
        const response = await postProduct(values);

      setMapsImage(response.data["maps_link"]);
      setHasBeenSearched(true);
      setX("");

    //   console.log(response.data["duration"]);
      
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className=" lg:h-5/6 md:h-3/4 sm:h-3/4 h-3/4 w-full  p-2  flex flex-col  rounded-xl justify-center items-center mx-5">
      <div className="  flex flex-col   p-2  justify-center items-center rounded-lg mt-1">
        <form>
          <div className=" flex flex-col p-2 items-center justify-center">
            <label htmlFor="x" className="text-gray-700 mainproba  text-sm items-center justify-center">
              Product ID:
            </label>
            <input
              type="text"
              id="x"
              name="x"
              className="p-2 border  inputbox rounded-lg  flex flex-col justify-center items-center"
              placeholder="Enter product ID"
              value={x}
              onChange={(e) => setX(e.target.value)}
            />
          </div>
          
        </form>
      </div>
      
      {!hasBeenSearched ? (
        <div className="lg:w-5/6  p-2 flex flex-col justify-center items-center">
          
          <button className="bg_color text-white p-2 rounded-lg w-1/2" onClick={handleClick}>
            Submit
          </button>
        </div>
      ) : (
        <div className="p-4 my-2 lg:w-5/6  lg:p-2 lg:flex lg:flex-col items-center justify-center">
            
            <img src={mapsLink} ></img>  
        </div>
        
      )}
    </div>
  );
}

export default ProductID;
