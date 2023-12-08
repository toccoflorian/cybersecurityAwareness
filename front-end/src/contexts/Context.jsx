import { createContext, useContext, useState } from "react";



export function DataProvider({ children }) {


    const tailleDisponibeContext = createContext();

    return (<>
        <DataProvider.provider value={tailleDisponibeContext}>
            {children}
        </DataProvider.provider>
    </>)
}