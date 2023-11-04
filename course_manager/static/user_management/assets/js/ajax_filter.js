// Wait for the document to be ready
$(document).ready(function () {
    
    function updateCourseList() {
        const letterFilter = $('#letter-filter').val();
        

        // Send an AJAX request to the server to filter 
        $.ajax({
            url: '/course/search/',  // Replace with the actual URL for your filter view
            method: 'GET',
            data: {
                letter: letterFilter,
                
            },
            success: function (data) {
                // Clear the teacher list
                

                $('#courses-list').empty();

                
                for (const course of data.courses) {
                    const listItem = $('<li>');
                    listItem.append($('<a>', {
                        href: `/course/${course.id}/`,  // Replace with the actual URL for course profiles
                        text: `${course.title}`,
                    }));
                    listItem.append($('<div>', {
                        type: 'button', // Specify 'button' type for the button element
                        class: 'btn-link', // Apply a CSS class for link styling (you can define this class in your CSS)
                        text: 'Edit',
                        on: {
                            click: function() {
                                // Redirect to the course's edit page when the button is clicked
                                window.location.href = `/course/edit/${course.id}/`; // Replace with the actual URL for course profiles
                            }
                        }
                        
                    }));
                    $('#course-list').append(listItem);
                }
            },
            error: function (error) {

                console.error('Error:', error);
            },
        });
    }

    // Event listeners for filter inputs
    $('#letter-filter').on('input', updateCourseList);
    

    // Initial Course list update on page load
    updateCourseList();
});
