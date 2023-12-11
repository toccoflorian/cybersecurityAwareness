import { useContext, useEffect, useState } from "react";
import { APIContext } from "../../APIServices/APIContext"

export default function Navigation() {

    const { fetchData, displayContent } = useContext(APIContext);
    const [inputContent, setInputContent] = useState("");

    function handleGoDir() {
        fetchData("go_dir", inputContent, "json")
    }

    function handleBack() {
        fetchData('go_back', null, "json")
    }


    return (<>
        <div className={`d-flex flex-column`}>


            <div className={`mb10`}>
                <p>Entrer dans un dossier enfant.</p>
                <p>Ne se terminant pas par &#34;@&#34;.</p>
                <input onChange={(e) => setInputContent(e.target.value)} type="text" />
                <button onClick={handleGoDir} className={`btn`} >Aller</button>
            </div>
            <p>Voir le dossier actuel et son contenu, tester la connexion et/ou rafraichir.</p>
            <button onClick={() => fetchData("get_current_dir", null, "json")} className={`btn`} >Voir</button>
            <p>Revenir dans le dossier parent.</p>
            <button onClick={handleBack} className={`btn`}>précedent</button>

        </div>
    </>)
}