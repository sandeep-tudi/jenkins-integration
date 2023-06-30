# this will printout even if the lent of the word is even
st= 'Print every word in this sentence that has as even number of letters'
for word in st.split():
    if len(word)%2 == 0:
        print(word+ ' is Even')
