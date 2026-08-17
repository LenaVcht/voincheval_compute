import streamlit as st

# ---------------------------------
#       COMPUTING FUNCTIONS
# ---------------------------------

def max_base_price(groceries_price, people_1d, people_2d): 
    max_base_price = groceries_price / (people_1d + 2*people_2d) or 1.0
    return max_base_price

def compute_final_prices(groceries_price, base_price, people_1d, people_2d, people_1d_alc, people_2d_alc) :
    people_1d_non_alc = people_1d - people_1d_alc
    people_2d_non_alc = people_2d - people_2d_alc

    alcohol_price = (groceries_price - (people_1d_non_alc + 2*people_2d_non_alc)*base_price) / (people_1d_alc + 2*people_2d_alc) - base_price

    return [{
        "1 jour - Pas d'alcool": "{:.2f}€".format(base_price),
        "1 jour - Alcool": "{:.2f}€".format(base_price+alcohol_price),
        "2 jours - Pas d'alcool": "{:.2f}€".format(2*base_price),
        "2 jours - Alcool": "{:.2f}€".format(2*(base_price+alcohol_price)),
    }]


# ---------------------------------
#            INTERFACE
# ---------------------------------
def main():
    st.write("""
    # Calcul - Fête du VOINCHEVAL
    Tous les ans, on se fait chier à faire des calculs, ça fait mal à la tête et c'est long, alors cette année on innove. Laissez-moi vous présenter le **super-calculateur-de-qui-doit-quoi-à-Julie !!!**
    """)

    st.info("Tout d'abord, entrons les informations inportantes (le prix des courses, le nombre de personnes présentes un seul soir, ou les deux, et celleux qui ont consommé de l'alcool).")

    with st.container(border=True) :
        # Groceries price input
        st.caption("Combien ont coûté les courses cette année ?")
        groceries_price = float(st.number_input("Prix des courses", 0, value=400, width=400, label_visibility="collapsed"))

        # Number of people input
        st.caption("Combien de personnes étaient présentes ?")
        people_data = [{
            "1 jour": 10,
            "Alcool - 1 jour": 5,
            "2 jours": 20,
            "Alcool - 2 jours": 15
        }]
        edited_data = st.data_editor(people_data, width="stretch", num_rows="fixed")

    people_1d = float(edited_data[0]["1 jour"])
    people_2d = float(edited_data[0]["2 jours"])
    people_1d_alc = float(edited_data[0]["Alcool - 1 jour"])
    people_2d_alc = float(edited_data[0]["Alcool - 2 jours"])

    # Slider to test 
    st.write("Et c'est maintenant que la véritable magie opère ! Vous pouvez déplacer le curseur pour voir les différents prix qui fonctionnent et choisir le plus équitable selon vous.")
    with st.container(border=True) :
        base_price = st.slider("**Prix de base :**", 0.0, max_base_price(groceries_price, people_1d, people_2d), step=0.5, format="euro")

        prices_data = compute_final_prices(
            groceries_price, base_price, people_1d, people_2d, people_1d_alc, people_2d_alc
        )

        st.write("Tarifs : ")
        st.dataframe(prices_data, width='stretch')

if __name__ == "__main__":
    main()
