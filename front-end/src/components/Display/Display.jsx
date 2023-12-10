import { useContext, useEffect, useState } from "react";
import styles from "./Display.module.scss";
import { APIContext } from "../../APIServices/APIContext";

export default function Display() {

    const { displayContent, fetchData } = useContext(APIContext);




    return (<>

        <div className={`${styles.displayContainer} `}>
            <ul>

                {displayContent.
                    map((element, index) => {
                        let newElement = [];
                        if (element.length > 1 && typeof element[1] !== "string") {
                            newElement = [element[0], ...element[1]]
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