def play():
    agents = ['SOVA', 'PHOENIX', 'BREACH', 'BRIMSTONE', 'YORU', 'CYPHER', 'REYNA', 'SAGE', 'ASTRA', 'KILLJOY', 'RAZE',
              'SKYE', 'OMEN']
    team = dict()
    while len(team.values()) < 5:
        for choice in range(1, 6, 1):
            print(f'available agents: {agents}')
            name = input('Type your username: ')
            selected_agent = input('Choice your agent: ').upper()

            found_agent = list(filter(lambda agent: agent in agents, agents))
            if found_agent:
                team[name] = selected_agent
                agents.remove(selected_agent)
                print(f'team: {team}')
            else:
                print('agent not found, please try again')


play()
