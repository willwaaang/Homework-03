import praw
import random
import datetime
import time

# FIXME:
# generate_comment functions from the week_07 lab
def generate_comment_0():
    trump_names = ['Donald Trump','Trump','Donald','The Trumpster','The Trump Truck']
    rtrump_names = random.choice(trump_names)
    feelabout = ['voted for','am voting for','will vote for','strongly support','support']
    rfeelabout = random.choice(feelabout)
    roles = ['the King of the World', 'the President of the United States', 'the President', 'the Prez']
    role = random.choice(roles)
    positivequality = ['he has nice feet', 'he has nice hair', 'I love his beautiful wife', 'he has nice eyes', 'he is rich']
    positivequalities = random.choice(positivequality)
    otherpositivequality = ['he has nice hands', 'he is hilarious', 'he is strong','I think he likes frogs', 'he is not poor']
    otherpositivequalities = random.choice(otherpositivequality)
    text = 'I ' + rfeelabout + ' ' + rtrump_names + ' as ' + role + ' because ' + positivequalities + '.' + ' Also, ' + otherpositivequalities + '.'
    return text

def generate_comment_1():
    trump_namess = ['Donald Trump','Trump','Donald','The Trumpster','The Trump Truck']
    rtrump_namess = random.choice(trump_namess)
    goodword = ['a fantastic', 'the right', 'the most suitable', 'the best', 'the coolest']
    rgoodword = random.choice(goodword)
    trumpname = ['Donald Trump','Trump','Donald','The Trumpster','The Trump Truck']
    rtrumpnames = random.choice(trumpname)
    compare = ['is much better than', 'is much more handsome than', 'has more hair than', 'is sexier than', 'is cooler than']
    rcompare = random.choice(compare)
    biden_names = ['that dude Biden', 'the Joe Joe Biden boy', 'Biden', 'Joe Biden', 'that other old man']
    rbiden_names = random.choice(biden_names)
    text = rtrump_namess + ' is ' + rgoodword + ' presidential candidate. ' + rtrumpnames + ' ' + rcompare + ' ' + rbiden_names + '.'
    return text

def generate_comment_2():
    trump_names = ['Donald Trump','Trump','Donald','The Trumpster','The Trump Truck']
    rtrump_names = random.choice(trump_names)
    feelabout2 = ['firmly believe', 'strongly believe', 'truly believe', 'think', 'know']
    rfeelabout2 = random.choice(feelabout2)
    positions = ['the best', 'the most well suited', 'the most handsome', 'totally the best', 'the smartest']
    position = random.choice(positions)
    positivequality2 = ['he has nice feet', 'he has nice hair', 'I love his beautiful wife', 'he has nice eyes', 'he is rich']
    positivequalities2 = random.choice(positivequality2)
    otherpositivequality2 = ['he is the best we have ever seen', 'he is the most qualified candidate ever', 'he is totally not racist', 'he is totally the best candidate ever', 'he is super awesome']
    otherpositivequalities2 = random.choice(otherpositivequality2)
    text = 'I ' + rfeelabout2 + ' that ' + rtrump_names + ' is ' + position + ' presidential candidate. ' + 'In fact, ' + otherpositivequalities2 + ' and ' + positivequalities2 + '.'
    return text

def generate_comment_3():
    biden_names = ['that dude Biden', 'the Joe Joe Biden boy', 'Biden', 'Joe Biden', 'the guy against my love, Trump']
    rbiden_names = random.choice(biden_names)
    negativefeelabout = ['did not vote for','am not voting for','will not vote for','am strongly against','am against']
    rnegativefeelabout = random.choice(negativefeelabout)
    roles = ['the next President', 'the President of the United States', 'the President', 'the Prez']
    role = random.choice(roles)
    negativequality = ['he does not have nice feet', 'he barely has any hair', 'I hate his wife', 'he does not have nice eyes', 'he is not as rich as trump']
    negativequalities = random.choice(negativequality)
    otherpositivequality = ['he does not have nice hands', 'he is not hilarious', 'he probably has dementia','he is not very handsome', 'he is not very tall']
    otherpositivequalities = random.choice(otherpositivequality)
    text = 'I ' + rnegativefeelabout + ' ' + rbiden_names + ' as ' + role + ' because ' + negativequalities + '.' + ' Also, ' + otherpositivequalities + '.'
    return text

def generate_comment_4():
    biden_namess = ['That dude Biden', 'The Joe Joe Biden boy', 'Biden', 'Joe Biden', 'The guy against my love, Trump']
    rbiden_namess = random.choice(biden_namess)
    badword = ['a terrible', 'the wrong', 'the worst', 'the worst possible', 'the uncoolest']
    rbadword = random.choice(badword)
    biden_namess = ['Mr. Biden', 'The Joe Joe Biden boy', 'Biden', 'Joe Biden', 'Big Biden']
    rbiden_namess = random.choice(biden_namess)
    compare = ['is much worse than', 'is much less handsome than', 'has less hair than', 'is less sexy than', 'is not as cool as']
    rcompare = random.choice(compare)
    trump_names = ['Donald Trump','Trump','Donald','The Trumpster','The Trump Truck']
    rtrump_names = random.choice(trump_names)
    text = rbiden_namess + ' is ' + rbadword + ' presidential candidate. ' + rbiden_namess + ' ' + rcompare + ' ' + rtrump_names + '.'
    return text

def generate_comment_5():
    bidens_names = ['that dude Biden', 'the Joe Joe Biden boy', 'Biden', 'Joe Biden', 'the guy against my love, Trump']
    rbidens_names = random.choice(bidens_names)
    feelabout2 = ['firmly believe', 'strongly believe', 'truly believe', 'think', 'know']
    rfeelabout2 = random.choice(feelabout2)
    negposition = ['the worst', 'not the best', 'not the most handsome', 'totally the worst', 'totally worse than Trump as a']
    negpositions = random.choice(negposition)
    negative = ['he has ugly feet', 'he has barely any hair', 'I do not love his beautiful wife', 'he does not have nice eyes', 'he is not very rich']
    negatives = random.choice(negative)
    othernegativequality2 = ['he is apparently the worst candidate we have ever seen', 'he is apparently the least qualified candidate ever', 'he totalllllllly has dementia', 'he is totalllllllly the worst candidate ever', 'he is totallllly super uncool']
    othernegativequalities2 = random.choice(othernegativequality2)
    text = 'I ' + rfeelabout2 + ' that ' + rbidens_names + ' is ' + negpositions + ' presidential candidate. ' + 'In fact, ' + negatives + ' and ' + othernegativequalities2 + '.'
    return text

def generate_comment():
    '''
    This function should randomly select one of the 6 functions above,
    call that function, and return its result.
    '''
    comments = [generate_comment_0, generate_comment_1, generate_comment_2, generate_comment_3, generate_comment_4, generate_comment_5] 
    text = random.choice(comments)()
    return text


# connect to reddit
reddit = praw.Reddit('bot')

# connect to the debate thread
reddit_debate_url = 'https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/'
submission = reddit.submission(url=reddit_debate_url)

# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

start_time = datetime.datetime.now()

while True:
# or use a for loop
# if True: 
# for i in range(5): # have to run more than once for Task 5 to work

    # printing the current time will help make the output messages more informative
    # since things on reddit vary wsith time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

        # if start_time - datetime.datetime.now() is > or equal to 30:
        #     break
        #use datetime now to check if 30 minutes has passed

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    submission.comments.replace_more(limit=None) # set limit = None to get all level comments, set = 1 while debugging/writing
    # for limit None, goes through entire comments
    all_comments = []
    
    all_comments = submission.comments.list()
    print('len(all_comments)=',len(all_comments))
    
    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    my_comments = []
    for comment in all_comments:
        if comment.author == 'MrCS40-Bot':
            my_comments.append(comment)
        else:
            not_my_comments.append(comment)


    print('len(not_my_comments)=',len(not_my_comments))
    print('len(my_comments)=',len(my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (you bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments)
    
        # post a top level comment
        # print(generate_comment())
        # submission.reply(generate_comment())

        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment

    if has_not_commented == len(all_comments):
        try:
            submission.reply(generate_comment())
        except: 
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')

        print(generate_comment())
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
 
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to

    else:
        comments_without_replies = []
        for comment in not_my_comments:
            replied = True
            for comment.reply in not_my_comments: 
                if comment.author == 'MrCS40-Bot':
                     replied = True
                     break 
                if comment.author != 'MrCS40-Bot':
                    replied = False 
            if replied:
                continue
            else:
                comments_without_replies.append(comment)         
        
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))
        
        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        try:
            try:
                # sorted_comments_without_replies = sorted(comments_without_replies key=comment.score) -- figure this part out
                comment = reddit.comment(id=random.choice(comments_without_replies))
                print('comment_id =', random.choice(comments_without_replies))
                comment.reply(generate_comment())
            except:
                pass
        except: #AssertionError
            print('exception found')
            print('starting to sleep')
            time.sleep(60)
            print('done sleeping')

        # print(generate_comment())
        # print(type(comments_without_replies))

        # use random.choice() with list 
        # also use submission.reply(generate_comment())

        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit
            
#Extra Credit Oppurtunities.
    # Upvote any comment mentioning your favorite candidate
    for comment in submission.comments.list():
        if 'biden' in comment.body.lower():
            comment.upvote()
            print('Comment Upvoted!')

    # Downvote any comment mentioning the opposition
    for comment in submission.comments.list():
        if 'trump' in comment.body.lower():
            comment.downvote()
            print('Comment Downvoted!')

    for submission in reddit.subreddit('csci040temp'):

        # Upvote any submission mentioning your favorite candidate
        if 'Biden' in submission.title.lower():
            submission.upvote()
            print('Submission Upvoted!')

        # Downvote any submission mentioning the opposition
        if 'Trump' in submission.title.lower():
            submission.downvote()
            print('Submission Downvoted!')

    # FIXME (task 5): select a new submission for the next iteration;
    
    result = random.random()
    all_submissions = []
    if result >= 0.5:
        print('original submission')
        submission = reddit.submission(url='https://www.reddit.com/r/csci040temp/comments/jm338w/another_debate_post/')
        submission.reply(generate_comment())
    if result < 0.5:
        print('top subreddit submission')
        # print(type(all_submissions))
        # for submission in reddit.subreddit("csci040").top("month"):
        for submission in reddit.subreddit("csci040temp").top("day"):

            all_submissions.append(submission)

        submission_choice = random.choice(all_submissions)
        submission = reddit.submission(id=submission_choice)
        print('submission_id =',submission_choice)
        print(submission_choice.title)
