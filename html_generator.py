def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '<h2>' + concept_title + '</h2>'
    html_text_2 = '''
    <div class="concept">
        ''' + concept_description
    html_text_3 = '''
    </div>
    '''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['MUTATION', ''' Lists support mutation (strings do NOT)- you can change the value of the list after it is created without creating a new object.  You assign a new value similar to index:
            List = ['Y','e','l','l','o']
            List[0] = 'H'
            Print List  returns ['H','e','l','l','o']
            Procedures don't need a return statement when replacing an item in a list.'''],
                             ['ALIASING', 'Two different variables are assigned to the same object - this is important to understand when debugging - you may have renamed or added a name to a variable.'],
                             ['Append', '''This is similar to the 'find' method and works like a procedure.  It mutates the list to add at the end of the list. It does NOT create a new list but edits the existing list.
            List = ['H','e','l','l','o']
            List.append('!')
            Print List  returns ['H','e','l','l','o','!']'''] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)