def find_champion_and_runner_up(scores):
    result = None
    # TODO: Enjoy your solving here
    champion = None
    runner_up = None
    if (scores != None) and (len(scores) < 2):
        raise Exception('The list must have at least two scores')
    else:
        champion = scores[0]
        runner_up = scores[1]
       
        if(champion < runner_up) :
            temp = champion
            champion = runner_up
            runner_up = temp
        
        for score in scores:
            if (score <= -100) or (score > 100):
                 raise Exception('Invalid scode ' + str(score) + '. ( -100 < x <=100)')
            elif score > champion:
                runner_up = champion
                champion = score
            elif (score > runner_up) and (score < champion):
                runner_up = score
        result = [champion, runner_up]
    return result


if __name__ == '__main__':
    scores = []
    # TODO: Collect input information from console here
    scstr = str(input("Input scores, each score separated by a space:"))
    lt = scstr.split(' ')
    scores = [int(score) for score in lt]

    print(find_champion_and_runner_up(scores))
