#This function will combine an HTML concept title with the description, 
#and add the apprpriate HTML tags and spaces.

def generate_concept_HTML(concept_title, concept_description):
    html_concept_title = '<h2>' + concept_title + '</h2>'
    html_concept_div_and_description = '''
    <div class="concept">
        ''' + concept_description
    html_close_description = '''
    </div>
    '''
    full_concept = html_concept_title + html_concept_div_and_description + html_close_description
    return full_concept

#This function pulls the first item in a list and assigns it to the variable 'concept_title'
#and the second item in a list and assigns it to the variable 'concept_description'.
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

#This is a list I generated from my class notes.  The first concept is to name and describe MUTATION
#The mutation description includes an example of how it works. The second concept describes ALIASING
#and the problem it may cause. The third concept describes APPEND and provides an example.
NOTES = [ ['MUTATION', ''' Lists support mutation (strings do NOT)- you can change the value of the list after it is created without creating a new object.  You assign a new value similar to index. Here is an example replacing 'Y' with 'H'.
            List = ['Y','e','l','l','o']
            List[0] = 'H'
            Print List  returns ['H','e','l','l','o']
            Procedures don't need a return statement when replacing an item in a list.'''],
        ['ALIASING', 'Two different variables are assigned to the same object - this is important to understand when debugging - you may have renamed or added a name to a variable.'],
        ['APPEND', '''This is similar to the 'find' method and works like a procedure.  It mutates the list to add at the end of the list. It does NOT create a new list but edits the existing list.
            List = ['H','e','l','l','o']
            List.append('!')
            Print List  returns ['H','e','l','l','o','!']'''] ]

#This final function creates a 'For Loop' that will repeat the function to make_HTML for every item in the list of concepts.
def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(NOTES)