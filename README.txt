
>>>>>>>>>>>>>>>>>>>>>>>>>>length of the file must not go beyond this line<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
====================
==Why my_utility repo?
===================

---utiltiy_code, example_code, hotkeys, config, commands

> I often forget usecase and keywords
> I notices that exmpale_code and utility_code helps increase my recall and overall productivity when
    relearn code or coding in general

====================
==About this repo
===================
> This repo contains all utilities that would be needed to migrate or use independent on location of computers
being used .
	such as 
		conda environment, pycharm configuration setup

> my_utility repo is decided for the ease of collabortion when other programmers/researchers.
    :to enhance group productivity.

NOTE:
    : style of this repo may change over time with ultimate goal of being as productive as possible.

====================
===Rules
====================
> my_utility repo must always be updated to github at the end of the day that changes are made.
> meta_files repo must always be updated to github at the end of the day that changes are made.
    :meta_files are files with prefix = "meta_"
    :meta_files manage "flow" of non_meta_files
        eg
            meta_todo_list manages todo_list (there are many todo_list to be managed)

> my_utility must always be used at all time whenever I code + read + learn + research.
> all of the folder under my_tility folder must contains README.txt
> README.txt must have the following sections
    : about folder_name
    : about folder_name
    : Rules

> research_related, example_code, utility_code, side_project must contains the following files
    :priority_list
        => order of the list is important
        => expected deadline for each must be provided
    :todo_list
        => todo_list is unprioritized priority_list
    :priority_list and todo_list must have no overlapped

    note:
        research_lated should also contain "progress_log"

> unfinihed tasks must include the following poitn
    :keyword
        =>to search for what I stuck on. it should be unique.
    :problem
        =>what am i stucking on
    :how to reproduce the problem(optional)
    :question to answer
        => these question should help me to solve the problem in the next attempt
    :note
        => includes everythings that are important such as url, resources, note to myself, observation etc.

----file naming convention
> all files must be in lower cases.
> naming should follow the following convention
    : topic_adjective
        => adjective must be general and reflect files and folders that it contains

======================
==How to use my_utility project
======================

#=====================
  Priority_list vs todo_list (NOT REQUIRED DEADLINE)
        vs
  Progress_log vs Productivity_log (REQUIRED DEADLINE)
#=====================

(NOT REQUIRED DEADLINE)
:Priority_list
    >Priority manages order in which tasks must be performed in sequence.
        note: if tasks must be skipped, ordered must first be adjust in the file accordingly
            to reflect the new orders.
:todo_list
    >todo_list is unordered priority_list.
        => multiple tasks that must be done in order must first be moved to priorty_list.
            note: priority_list and todo_list must have no overlapped

(REQUIRED DEADLINE)
:Productivity_log
    >Productivity_log keeps track of time that is used productivity towords tasks within
        "Priority_list"
:Progress_log
    >Progress_log keeps track of finished and unfinished tasks
        =>date of deadline for all tasks must be specified.
            ,but time of the date is optional
note: Productivity_log and Progress_log differs in that one is time oriented and another is
    tasks oriented.
=====================
==Priority_list, todo_list  (NOT ORDERED BY TIME)
=====================
>priority_list
    : order of the list is important
    : expected deadline for each must be provided

>todo_list
    :todo_list is unprioritized priority_list

note: priority_list and todo_list must have no overlapped

=======================
==Progress_log, productivity_log (ORDERED BY TIME)
=======================
>progress_log
    :progress_log tracks whether or not deadline of task assigned for the week is satistified
    :tasks that are qualified to be in progress_log must be tasks with specific conditions
    eg
        for research papers reading list,
            :read "number" papers on "some_topic" , summarize papers by main finding and categorized them by keywords
                >paper1
                    >>summarize paper1
                    >>categorized paper1
                >paper2
                    >>summarize paper2
                    >>categorized paper2
                >paper3
                    >>summarize paper3
                    >>categorized paper13

            notice: notice that reading task is very specific and within the tasks there are subtasks
                that can be done progressively

    :progress_log must have the following format
        eg
            => 8-19-19
                >paper1
                    >>summarize paper1
                    >>categorized paper1
                >paper2
                    >>summarize paper2
                    >>categorized paper2
            => 8-19-19
                >do deep learning hw1
                    >>question1
                    >>question2
                    ...
            ...

>total_productivity_log
    :total_productivity_log records total_productivity_log up until now
    :total_productivity_log must have the following format
        eg
        >8-25-19
            :weekly productiZvity_hour
                => 8-19-19
                    productivity hour = 10 hrs
                    =>> details...
                    =>> details...
                => 8-20-19
                    productivity hour = 10 hrs
                    =>> details...
                    =>> details...

>weekly_productivity_log
    :new_productivity_log must have the following format
        eg
            >8-19-19
                :weekly_productivity hour = 10 hrs
                    >details...
                    >details...
                    >details...
                    >details...

    :productivity that hasn't been updated to productivity_log
    :it must be update daily or before sleep
    :at the beginning of every week weekly_productivity_log should be empty. (renew every week)

