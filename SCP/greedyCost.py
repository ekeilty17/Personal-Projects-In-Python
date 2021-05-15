
# Algorithm is trying to balance sets covered and cost of using the set
# Essentially minimizes this quanitity
#       Cost(E) / | diff(E, s) |
def greedyCost(U, S, coverage):
    # U = universal set
    # S = set of subsets
    # coverage = percent of U that we want to over with sets in S

    u = U.copy()
    # u is the 'reduced universal set'
    #   As we cover more elements, we remove elements that have already been covered
    s = S.copy()
    # s is the 'reduced set of subsets'
    #   As we choose sets, we need to remove ones that we have alreayd used

    Cover = set([])
    # Output of the function

    alpha = 1 - float(len(u))/float(len(U))

    while alpha < coverage:

        # Finding minimum value of Cost(E) / | diff(E, s) |
        min_cost = None
        min_cost_set = None
        for E in s:
            
            # If E doesn't cover any of u, go to next set
            if len(E.getElements().difference(s)) == 0:
                continue

            curr_set_cost = float(E.getCost()) / float( len(E.getElements().difference(s)) )
            if min_cost == None:
                min_cost = curr_set_cost
                min_cost_set = E
            elif curr_set_cost < min_cost:
                min_cost = curr_set_cost
                min_cost_set = E

        # If no sets were chosen, then we are done
        if min_cost_set == None:
            break

        Cover.add(min_cost_set)                       # Adding chosen set to output
        u = u.difference(min_cost_set.getElements())  # removing covered elements
        s.remove(min_cost_set)                        # removing chosen set from list of next possible sets

        alpha = 1 - float(len(u))/float(len(U))

    return Cover
