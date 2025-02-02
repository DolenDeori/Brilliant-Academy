import { useEffect, useState } from "react";
import Navigation from "./components/Navigation";
// import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  // const apiUrl = import.meta.env.VITE_API_URL;
  // console.log(apiUrl);
  // let datares;
  // axios
  //   .get(`${apiUrl}admission_form/`)
  //   .then((res) => {
  //     datares = res.data;
  //     setData(datares);
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
  return (
    <>
      <Navigation />
      <div className="h-svh w-full flex justify-center items-center gap-2 flex-col">
        {data.map((items) => (
          <div key={items.id} className="p-4 bg-gray-800 text-white rounded">
            <h1>First Name: {items?.first_name}</h1>
            <h1>Last Name: {items?.last_name}</h1>
            <p>Phone Number: {items?.phone_number}</p>
          </div>
        ))}
      </div>
    </>
  );
}

export default App;
