import { useContext, useState } from "react";
import { APIContext } from "../../APIServices/APIContext";



export default function Execute() {

    const { fetchData, displayContent } = useContext(APIContext);
    const [inputContent, setInputContent] = useState('')

    function handleClick() {
        fetchData("execute", inputContent, "json")
    }


    return (<>
        <div className={`button-container`}>
            <p>Executer un fichier (.exe, .png, txt...) ou une ligne de commande</p>
            <p className={`infos-text`}>Se terminant par &#34;@&#34; pour les fichiers</p>
            <p className={`infos-text`}>sinon entrez votre ligne de commande.</p>
            <input onChange={(e) => setInputContent(e.target.value)} type="text" />
            <button onClick={handleClick} className={`btn`} >Exécuter</button>
        </div>
    </>)
}