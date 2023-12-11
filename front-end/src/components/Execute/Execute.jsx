import { useContext, useState } from "react";
import { APIContext } from "../../APIServices/APIContext";



export default function Execute() {

    const { fetchData, displayContent } = useContext(APIContext);
    const [inputContent, setInputContent] = useState('')

    function handleClick() {
        fetchData("execute", inputContent, "json")
    }


    return (<>
        <div>
            <p>Executer un fichier (.exe, .png, txt...)</p>
            <p>Se terminant par &#34;@&#34;.</p>
            <input onChange={(e) => setInputContent(e.target.value)} type="text" />
            <button onClick={handleClick} className={`btn`} >Execute</button>
        </div>
    </>)
}