#There's a need to have the floor list itself be reactive...
#Read up on event listeners

from dominate import document, tags

with document() as doc:
    with doc.head:
        tags.meta(charset = 'utf-8')
        tags.meta(
            name = 'viewport',
            content = 'width = device-width, initial-scale = 1'
        )
        tags.link(
            href = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css',
            rel = 'stylesheet',
            integrity = 'sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN',
            crossorigin = 'anonymous',
        )
        tags.link(
            href = 'https://cdn.jsdelivr.net/npm/daterangepicker/daterangepicker.css',
            rel = 'stylesheet',
            type = 'text/css',
        )
        tags.link(href = 'stylesheet.css', rel = 'stylesheet')
        tags.script(
            type = 'text/javascript',
            src = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js',
            integrity = 'sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL',
            crossorigin = 'anonymous',
        )
        tags.script(
            type = 'text/javascript',
            src = 'https://code.jquery.com/jquery-3.7.1.min.js',
            integrity = 'sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=',
			crossorigin = 'anonymous',
        )
        tags.script(
            type = 'text/javascript',
            src = 'https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.30.1/moment.min.js',
            crossorigin = 'anonymous',
        )
        tags.script(
            type = 'text/javascript',
            src = 'https://cdn.jsdelivr.net/npm/daterangepicker/daterangepicker.min.js',
            crossorigin = 'anonymous',
        )
    
    with doc.body:
        with tags.div(cls = 'container'):
            with tags.div(cls = 'row'):
                with tags.div(cls = 'col-3'):
                    tags.input_(
                        type = 'text',
                        id = 'date_range',
                        value = '',
                    )
                    tags.script(
                        """
                        $(function() {

                          $('input[name=\"date_range\"]').daterangepicker({
                              autoUpdateInput: false,
                              locale: {
                                  cancelLabel: 'Clear'
                              }
                          });

                          $('input[name=\"date_range\"]').on('apply.daterangepicker', function(ev, picker) {
                              $(this).val(picker.startDate.format('MM/DD/YYYY') + ' - ' + picker.endDate.format('MM/DD/YYYY'));
                          });

                          $('input[name=\"date_range\"]').on('cancel.daterangepicker', function(ev, picker) {
                              $(this).val('');
                          });

                        });
                        """
                    )
                    
                with tags.div(cls = 'col-9'):
                    pass
            with tags.div(cls = 'row'):
                with tags.div(cls = 'col-3'):
                    with tags.div(
                        id = 'floor_buttons',
                        cls = 'btn-group-vertical',
                    ):
                        tags.button(
                            type = 'button',
                            cls = 'btn floor_btn btn-outline-primary active',
                            data_image = 'floor_plans/friends.jpg',
                        )
                        tags.button(
                            type = 'button',
                            cls = 'btn floor_btn btn-outline-primary',
                            data_image = '2',
                        )
                        tags.button(
                            type = 'button',
                            cls = 'btn floor_btn btn-outline-primary',
                            data_image = '3',
                        )
                with tags.div(cls = 'col-9'):
                    tags.canvas(
                        id = 'canvas', 
                        width = 300, 
                        height = 150,
                    )
        tags.script(src = 'listener_functions.js')
        tags.script(src = 'floor_button_setup.js')
    
    print(doc)
    with open("index.html", "w") as f:
        f.write(doc.render())

exit()

doc = document()

with doc.head:
    tags.link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css")
    

with doc:
    with div(cls='btn-group-vertical', role='group', aria_label='example'):
        button('Option 1', type='button', cls='btn btn-secondary', onclick='selectRadio(1)')
        
        button('Option 2', type='button', cls='btn btn-secondary', onclick='selectRadio(2)')
        
        button('Option 3', type='button', cls='btn btn-secondary', onclick='selectRadio(3)')

    script().add("""
        function selectRadio(option) {
            // Set the corresponding radio input to checked
            console.log(option)
            //document.querySelector('input[name="options"][value="' + option + '"]').checked = true;
            
            // You can get the selected value using the radio input's value
            // For example: var selectedValue = document.querySelector('input[name="options"]:checked').value;
        }
    """)

# Save the HTML document to a file
with open("index.html", "w") as f:
    f.write(doc.render())

# Step 3: Create an HTML document
# doc = document()

# # Step 4: Add a title to the document
# with doc.head:
    # tags.title("My Bootstrap Page")

# # Step 5: Add Bootstrap CDN links
# with doc.head:
    # tags.link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css")
    # tags.script(src="https://code.jquery.com/jquery-3.5.1.slim.min.js")
    # tags.script(src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js")
    # tags.script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js")
    # tags.script(src="script.js")

# with doc:
    # with tags.div(cls = 'btn-group-vertical', aria_label = "example"):
        # tags.button('1', type = 'button', cls = 'btn btn-secondary', onclick = 'toggleButton(this)')
        # tags.button('2', type = 'button', cls = 'btn btn-secondary', onclick = 'toggleButton(this)')
        # tags.button('3', type = 'button', cls = 'btn btn-secondary', onclick = 'toggleButton(this)')
        

# # Step 6: Create the body of the document
# # with doc:
    # # # Add a Bootstrap container
    # # with div(cls="container"):
        # # # Add a Bootstrap navbar
        # # with nav(cls="navbar navbar-expand-lg navbar-light bg-light"):
            # # a("My Bootstrap Page", cls="navbar-brand", href="#")
            # # with div(cls="collapse navbar-collapse", id="navbarNav"):
                # # with ul(cls="navbar-nav"):
                    # # li(a("Home", cls="nav-item nav-link active", href="#"))
                    # # li(a("About", cls="nav-item nav-link", href="#"))
                    # # li(a("Contact", cls="nav-item nav-link", href="#"))

        # # # Add a Bootstrap jumbotron
        # # with div(cls="jumbotron"):
            # # h1("Hello, world!", cls="display-4")
            # # p("This is a simple Bootstrap page generated using the dominate package in Python.", cls="lead", id = "example")
            # # hr(cls="my-4")
            # # p("It uses the Bootstrap stylesheet for styling and jQuery for some interactive elements.")
            # # button("Try it", type = "button", onclick = "myFunction()")

# # Step 7: Save the HTML document to a file
# with open("index.html", "w") as f:
    # f.write(doc.render())