export const formatDate = (date) => {

    let split_date
    let today

    if (date === null) return null
    if (typeof(date) !== 'object') {
        split_date = date.split('.')
        today = new Date(split_date[2], split_date[1], split_date[0]);
    } else {
        today = date
    }

    const yyyy = today.getFullYear();
    let mm = today.getMonth() + 1; // Months start at 0!
    let dd = today.getDate();

    if (dd < 10) dd = '0' + dd;
    if (mm < 10) mm = '0' + mm;

    const formattedToday = dd + '.' + mm + '.' + yyyy;
    return formattedToday
}