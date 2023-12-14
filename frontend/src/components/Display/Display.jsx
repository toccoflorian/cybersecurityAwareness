import { useContext } from "react";
import styles from "./Display.module.scss";
import { APIContext } from "../../APIServices/APIContext";

export default function Display() {

    const { displayContent, fetchData } = useContext(APIContext);




    return (<>
        <div className={`d-flex justify-space-b`}>
            <p className={`white`}>OUTPUT:</p >

        </div>

        <div className={`${styles.displayContainer} `}>
            <ul>
                {/* double map pour mettre en forme le rendu final */}
                {displayContent.
                    map((element, index) => {
                        let newElement = [];
                        if (element.length > 1 && typeof element[1] !== "string") { // si 'element' n'est pas une string et est composé de plus de 1 element
                            newElement = [element[0], ...element[1]] // element: [string, [string, string]] 
                        } else {
                            newElement = element
                        }

                        return <li key={index}>{typeof newElement !== "object" ?
                            newElement
                            :
                            <ul> CONTENU: {newElement.
                                map((element, index) => <li key={index}>{element}</li>)}</ul>}</li>
                    })}
            </ul>
        </div>
    </>)
}