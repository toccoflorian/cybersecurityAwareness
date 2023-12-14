import { useContext, useState } from "react"
import { APIContext } from "../../APIServices/APIContext";


export default function Download() {

    const { fetchData, displayContent } = useContext(APIContext);
    const [inputContent, setInputContent] = useState('')

    function handleClick() {
        fetchData("download", inputContent, "json")
    }

    return (<>
        <div className={`button-container`}>
            <p>Télécharger un fichier.</p>
            <p className={`infos-text`}>Se terminant par &#34;@&#34;.</p>
            <input onChange={(e) => setInputContent(e.target.value)} type="text" />
            <button onClick={handleClick} className={`btn`} >Télécharger</button>
        </div>
    </>)
}