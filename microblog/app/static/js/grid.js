






$('#grid').w2grid({
    name: 'grid',
    header: 'List of Posts',
    show: {
        toolbar: true,
        footer: true
    },
    columns: [
        { field: 'id', caption: 'ID', size: '50px', sortable: true, attr: 'align=center' },
        { field: 'title', caption: 'Title', size: '30%', sortable: true, resizable: true },
        '''{ field: 'fname', caption: 'First Name', size: '30%', sortable: true, resizable: true },'''

    ],
    searches: [
        { field: 'lname', caption: 'Last Name', type: 'text' },
        { field: 'fname', caption: 'First Name', type: 'text' },
        { field: 'email', caption: 'Email', type: 'text' },
    ],sortData: [{ field: 'recid', direction: 'ASC' }],
    records: [
        
    ]
}); 