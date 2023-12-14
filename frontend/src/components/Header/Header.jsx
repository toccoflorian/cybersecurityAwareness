
import styles from "./Header.module.scss";

export default function Header() {


    return (<>
        <header>

            <h1 className={`text-center`}>Démonstration de vulnérabilités</h1>
            <p className={`text-center`}>Sensibilisation à la cybersécurité</p>

        </header>
        <div className={`${styles.contactDev}`}>
            <p className={`white`}>Conçu et développer par Florian TOCCO</p>
            <p className={`white`}>https://www.malt.fr/profile/floriantocco</p>
        </div>
    </>)
}