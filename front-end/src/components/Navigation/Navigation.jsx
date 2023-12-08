

export default function Navigation() {

    return (<>
        <div className={`d-flex flex-column`}>

            <div className={`mb10`}>

                {/* <button className={`btn`}>aller dans</button> */}
                <select defaultValue="" placeholder="Aller dans le répertoire">
                    <option disabled value="">Aller dans le répertoire</option>
                    <option value="2">nom de repertoire</option>
                    <option value="3">nom de repertoire</option>
                </select>
            </div>

            <button className={`btn`}>précedent</button>

        </div>
    </>)
}