<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Expense Data</title>
</head>
<body>
    <div class="container mt-5">
        <div class="row">
            <div class="col-md-12">
                <?php
                    if (session()->getFlashdata('status')) {
                        $status = session()->getFlashdata('status');
                        echo '<div class="alert alert-info" role="alert">' . $status . '</div>';
                    }
                ?>

                <div class="card">
                    <div class="card-header">
                        <h4>Expense Data 
                            <a href="<?= base_url('expense_add')?>" class="btn btn-primary float-right">Add Expense</a>
                        </h4>
                    </div>
                    <div class="card-body">
                        <div class="table-responsive">
                            <table class="table table-bordered">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th>Name</th>
                                        <th class="d-none d-sm-table-cell">Photo</th>
                                        <th>Phone</th>
                                        <th class="d-none d-sm-table-cell">Amount</th>
                                        <th>Expense</th>
                                        <th>Total Expense</th>
                                        <th class="d-none d-sm-table-cell">Date</th>
                                        <th>Action</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <?php foreach($expenses as $row) :?>
                                        <tr>
                                            <td><?= $row['id'] ?></td>
                                            <td><?= $row['name'] ?></td>
                                            <td>
                                                <img src="<?= "uploads/". $row['photo'] ?>" alt="Expense Photo" width="50px" height="50px">
                                            </td>
                                            <td><?= $row['phone'] ?></td>
                                            <td class="d-none d-sm-table-cell"><?= $row['amount'] ?></td>
                                            <td><?= $row['expense'] ?></td>
                                            <td><?= $row['total_expense'] ?></td>
                                            <td class="d-none d-sm-table-cell"><?= $row['date'] ?></td>
                                            <td>
                                                <div class="btn-group" role="group">
                                                    <a href="<?= base_url('expense/edit/'.$row['id'])?>" class="btn btn-success btn-sm">Edit</a>
                                                    <form action="<?= base_url('expense/delete/'.$row['id'])?>" method="post">
                                                        <input type="hidden" name="_method" value="DELETE">
                                                        <button type="submit" class="btn btn-danger btn-sm">DELETE</button>
                                                    </form>
                                                    
                                                    <a href="<?= base_url('expense/download/'.$row['id']) ?>" class="btn btn-secondary btn-sm">Download</a>

                                                </div>
                                            </td>
                                        </tr>
                                    <?php endforeach; ?>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
</body>
</html>
