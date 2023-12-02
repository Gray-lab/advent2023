program day1_part1
    implicit none
    character(len=100) :: line
    character(len=1) :: firstDigit, lastDigit
    character(len=2) :: rowValueString
    integer :: unitNumber, iostat, i, rowValue, total

    open(newUnit=unitNumber, file='input.txt', status='old', iostat=iostat)

    ! check for errors in opening file
    if (iostat /= 0) then
        print *, "Error opening file."
        stop
    end if

    total = 0
    ! process each line
    do
        read(unitNumber, *, iostat=iostat) line
        if (iostat /= 0) exit
        ! iterate forwards
        do i = 1, len(line)
            if (line(i:i) > '0' .and. line(i:i) <= '9') then
                firstDigit = line(i:i)
                exit
            end if
        end do

        ! iterate backwards
        do i = len(line), 1, -1
            if (line(i:i) > '0' .and. line(i:i) <= '9') then
                lastDigit = line(i:i)
                exit
            end if
        end do

        rowValueString = firstDigit // lastDigit
        read (rowValueString, *) rowValue
        total = total + rowValue
    end do

    print *, "Total:", total
    close(unitNumber)
        
end program day1_part1