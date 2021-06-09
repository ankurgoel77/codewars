# https://www.codewars.com/kata/52996b5c99fdcb5f20000004

def runoff(voters):
    if not voters:
        return None

    # First, loop through all the sublists and create a dictionary with all the available candidates
    candidates = {}
    for ballot in voters:
        for candidate in ballot:
            if not candidate in candidates:
                candidates[candidate] = 0

    # Second, only count votes for first-choice candidates on each ballot
    for ballot in voters:
        candidates[ballot[0]] += 1

    # Sort this dictionary into a list of tuples by numbers of first-choice votes
    first_choice = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

    # If we have a winner, return it, otherwise, remove all lowest vote candidates and recurse
    if first_choice[0][1] > len(voters) / 2:
        return first_choice[0][0]
    else:
        least_common_count = first_choice[-1][1]
        least_common_candidates = [candidate for candidate,num_votes in first_choice if num_votes==least_common_count]
        new_voters = []
        for ballot in voters:
            new_ballot = []
            for candidate in ballot:
                if not candidate in least_common_candidates:
                    new_ballot.append(candidate)
            if new_ballot:
                new_voters.append(new_ballot)
        return runoff(new_voters)