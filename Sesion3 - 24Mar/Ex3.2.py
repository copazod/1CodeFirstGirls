mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'
affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'
should_visit_mars = is_willing and not can_afford
print('You should visit Mars: {}'.format(should_visit_mars))