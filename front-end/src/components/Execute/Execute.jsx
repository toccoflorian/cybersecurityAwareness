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
            <p>Elements se terminant par &#34;@&#34;.</p>
            <input onChange={(e) => setInputContent(e.target.value)} type="text" />
            <button onClick={handleClick}>Execute</button>
        </div>
    </>)
}