import { useContext } from "react";
import { APIContext } from "./APIContext";


// export async function fetchData(endpoint = null, returnType = null) {


//     let url = "http://127.0.0.1:12000/";
//     endpoint && (url = url + endpoint)
//     console.log(url);
//     const response = await fetch(url, {
//         method: "GET",

//     })

//     switch (returnType) {
//         case "json":
//             return response.json();
//         case "byte":
//             return response.body;

//         default:
//             return response.text();
//     }

// }