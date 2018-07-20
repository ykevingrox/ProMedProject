from summa.keywords import keywords

f = open('asdfghj.txt','r')
text = f.read()
# Calculate keywords

generated_keywords = keywords(text,scores = True)
print(generated_keywords)
# To be compared to the reference.
#reference_keywords = get_text_from_test_data("mihalcea_tarau.kw.txt").split("\n")

#self.assertEqual({str(x) for x in generated_keywords}, {str(x) for x in reference_keywords})